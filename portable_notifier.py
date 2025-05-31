#!/usr/bin/env python3
"""
Portable Notifier - 便携式通知器
可以复制到任何项目中使用，无需安装
"""

import requests
import functools
from datetime import datetime
from typing import Callable, Any
import os

class PortableNotifier:
    """便携式通知器类"""
    
    def __init__(self, ntfy_topic: str = None, ntfy_server: str = "https://ntfy.sh"):
        # 优先使用环境变量
        self.ntfy_topic = ntfy_topic or os.getenv("NTFY_TOPIC", "test")
        self.ntfy_server = ntfy_server or os.getenv("NTFY_SERVER", "https://ntfy.sh")
        self.ntfy_url = f"{self.ntfy_server}/{self.ntfy_topic}"
    
    def send_notification(self, title: str, message: str, status: str = "completed") -> bool:
        """发送通知"""
        try:
            status_config = {
                "completed": {"icon": "[OK]", "priority": "default"},
                "error": {"icon": "[ERROR]", "priority": "high"},
                "stopped": {"icon": "[STOP]", "priority": "default"},
                "started": {"icon": "[START]", "priority": "default"}
            }
            
            config = status_config.get(status, status_config["completed"])
            
            headers = {
                "Title": f"{config['icon']} {title}",
                "Priority": config["priority"],
                "Tags": f"task,{status}",
                "Timestamp": str(int(datetime.now().timestamp()))
            }
            
            response = requests.post(
                self.ntfy_url,
                data=message.encode('utf-8'),
                headers=headers,
                timeout=10
            )
            
            if response.status_code == 200:
                print(f"[OK] Notification sent: {title}")
                return True
            else:
                print(f"[ERROR] Failed to send notification: {response.status_code}")
                return False
                
        except Exception as e:
            print(f"[ERROR] Error sending notification: {e}")
            return False

# 全局实例
_notifier = PortableNotifier()

def notify(title: str, message: str, status: str = "completed") -> bool:
    """便捷通知函数"""
    return _notifier.send_notification(title, message, status)

def notify_task(task_name: str = None, notify_start: bool = True, notify_end: bool = True):
    """任务通知装饰器"""
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            actual_task_name = task_name or func.__name__
            start_time = datetime.now()
            
            if notify_start:
                _notifier.send_notification(
                    f"Task Started: {actual_task_name}",
                    f"Task started: {actual_task_name}\nStart time: {start_time.strftime('%Y-%m-%d %H:%M:%S')}",
                    "started"
                )
            
            try:
                result = func(*args, **kwargs)
                
                if notify_end:
                    end_time = datetime.now()
                    duration = end_time - start_time
                    _notifier.send_notification(
                        f"Task Completed: {actual_task_name}",
                        f"Task completed: {actual_task_name}\n"
                        f"Duration: {duration.total_seconds():.2f} seconds",
                        "completed"
                    )
                
                return result
                
            except Exception as e:
                if notify_end:
                    end_time = datetime.now()
                    duration = end_time - start_time
                    _notifier.send_notification(
                        f"Task Failed: {actual_task_name}",
                        f"Task failed: {actual_task_name}\n"
                        f"Error: {str(e)}\n"
                        f"Duration: {duration.total_seconds():.2f} seconds",
                        "error"
                    )
                raise
        
        return wrapper
    return decorator

# 使用示例
if __name__ == "__main__":
    # 测试通知
    notify("Portable Notifier Test", "Portable notifier is working!")
    
    # 测试装饰器
    @notify_task("Test Task")
    def test_function():
        import time
        time.sleep(1)
        return "Success"
    
    result = test_function()
    print(f"Result: {result}") 