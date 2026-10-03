import json
import os

def analyze_log(filepath: str) -> dict:
    # 结果字典建好
    result = {}
    result["total"] = 0
    result["by_level"] = {}
    result["by_user"] = {}
    result["last_error"] = None

    # 文件不在直接返回
    if os.path.exists(filepath) == False:
        return result

    # 打开文件
    f = open(filepath, "r", encoding="utf-8")
    for line in f:
        line = line.strip()
        if line == "":
            continue

        
        try:
            log = json.loads(line)
        except json.JSONDecodeError:
            continue
        except ValueError:
            continue

        
        result["total"] = result["total"] + 1

        
        level = log["level"]
        if level in result["by_level"]:
            result["by_level"][level] = result["by_level"][level] + 1
        else:
            result["by_level"][level] = 1

        
        user = log["user"]
        if user in result["by_user"]:
            result["by_user"][user] = result["by_user"][user] + 1
        else:
            result["by_user"][user] = 1

        
        if level == "ERROR":
            result["last_error"] = log["message"]

    f.close()
    return result