# Portable Notification System - Quick Guide

## 🚦 Prerequisites

- **Python ** 
- **ntfy** notification server (public: https://ntfy.sh or your own)

Install requests:
```bash
pip install requests
```

## 🎯 Overview

This is a super simple notification system for Python. With just one file (`portable_notifier.py`), you can add instant notifications to any Python project using decorators or function calls.

## 🚀 Quick Start

### Step 1: Copy the file
```bash
# Copy to your project directory
cp portable_notifier.py /your/project/path/
```

### Step 2: Use the decorator
```python
from portable_notifier import notify_task, notify

@notify_task("Data Processing Task")
def process_data():
    """This function will automatically send start and completion notifications."""
    # Your code here
    pass

# Call the function - notifications will be sent automatically
result = process_data()
```

That's it! 🎉

## 📋 Usage

### 1. Basic Decorator
```python
from portable_notifier import notify_task

@notify_task("My Task")
def my_function():
    import time
    print("Running task...")
    time.sleep(2)  # Simulate work
    return "done"

# Will automatically send: start notification → run → completion notification
result = my_function()
```

### 2. Custom Notification Options
```python
# Only notify on completion
@notify_task("Silent Task", notify_start=False, notify_end=True)
def silent_task():
    pass

# Only notify on start
@notify_task("Startup Task", notify_start=True, notify_end=False)
def startup_task():
    pass
```

### 3. Manual Notifications
```python
from portable_notifier import notify

notify("Task Complete", "Data processing finished!")
notify("Error Alert", "Something went wrong", "error")
notify("System Stopped", "Service has stopped", "stopped")
```

### 4. Automatic Error Handling
```python
@notify_task("Risky Task")
def risky_task():
    if some_condition:
        raise Exception("Task failed")  # Will automatically send error notification
    return "success"
```

## 🔧 Configuration Options

### Environment Variables (optional)
```bash
# Set your ntfy topic
export NTFY_TOPIC="your_custom_topic"

# Use a custom ntfy server
export NTFY_SERVER="https://your-ntfy-server.com"
```

### In-Code Configuration (optional)
```python
from portable_notifier import PortableNotifier

# Create a custom notifier
custom_notifier = PortableNotifier(
    ntfy_topic="my_project",
    ntfy_server="https://ntfy.sh"
)
```

## 📱 Notification Types

- **started**: Task started
- **completed**: Task completed successfully
- **error**: Task failed
- **stopped**: Task was stopped

## 💡 Example Use Cases

### Data Science
```python
@notify_task("Model Training")
def train_model():
    # Long-running training
    pass

@notify_task("Data Cleaning")
def clean_data():
    # Heavy data processing
    pass
```

### Automation Scripts
```python
@notify_task("Daily Backup")
def daily_backup():
    # Backup important files
    pass

@notify_task("System Check")
def system_check():
    # Check system status
    pass
```

### File Processing
```python
@notify_task("Batch Conversion")
def convert_files():
    # Convert many files
    pass
```

## ✨ Features

- **Zero config**: Just copy the file and use
- **Automatic notifications**: Decorator handles start/completion/error
- **Cross-platform**: Works on Windows, Linux, macOS
- **Lightweight**: Only one file, no extra dependencies
- **Flexible**: Supports environment variables and code config
- **Error handling**: Automatically catches and reports task failures

## 🎯 Best Practices

1. **Descriptive task names**: Use clear, meaningful names
2. **Reasonable notification frequency**: Avoid spamming
3. **Let the decorator handle errors**: No need for extra try/except unless you want custom logic
4. **Use environment variables**: For different environments or topics

That's all! One file for all your notification needs! 🚀 
