#!/usr/bin/env python3
"""
Notification Decorator Example - example.py
Demonstrates how to use portable notifier in regular code
"""

# Import notifier
from portable_notifier import notify_task, notify
import time
import random

# Example 1: Basic decorator usage
@notify_task("Data Processing")
def process_data(size=1000):
    """Process data - automatically sends start and completion notifications"""
    print(f"Starting to process {size} records...")
    
    # Simulate data processing
    for i in range(5):
        time.sleep(0.3)
        progress = (i + 1) * 20
        print(f"Progress: {progress}%")
    
    print("Data processing completed!")
    return {"processed": size, "success": True}

# Example 2: Only notify on completion
@notify_task("File Upload", notify_start=False, notify_end=True)
def upload_file(filename):
    """Upload file - only sends notification on completion"""
    print(f"Uploading file: {filename}")
    time.sleep(1.5)  # Simulate upload time
    print(f"File {filename} uploaded successfully!")
    return f"uploaded_{filename}"

# Example 3: Task that might fail
@notify_task("Network Request")
def fetch_data():
    """Network request - might fail, automatically sends error notification"""
    print("Sending network request...")
    time.sleep(1)
    
    # 30% chance of failure
    if random.random() < 0.3:
        raise Exception("Network connection timeout")
    
    print("Data fetched successfully!")
    return {"data": "some_important_data", "status": "ok"}

# Example 4: Long-running task
@notify_task("Model Training")
def train_model():
    """Simulate model training - long-running task"""
    print("Starting model training...")
    
    epochs = 3
    for epoch in range(epochs):
        print(f"Training epoch {epoch + 1}/{epochs}")
        time.sleep(1)  # Simulate training time
        
        # Simulate training steps
        for step in range(3):
            time.sleep(0.5)
            print(f"  Step {step + 1}/3 completed")
    
    print("Model training completed!")
    return {"model": "trained_model.pkl", "accuracy": 0.95}

# Example 5: Batch processing
@notify_task("Batch Processing")
def batch_process():
    """Batch process multiple tasks"""
    tasks = ["Task A", "Task B", "Task C", "Task D"]
    results = []
    
    print(f"Starting batch processing of {len(tasks)} tasks...")
    
    for i, task in enumerate(tasks, 1):
        print(f"Processing {task} ({i}/{len(tasks)})")
        time.sleep(0.8)
        results.append(f"{task}_completed")
    
    print("Batch processing completed!")
    return results

def main():
    """Main function - run all examples"""
    
    print("🚀 Notification Decorator Example Program")
    print("=" * 50)
    
    # Send start notification
    notify("Example Program Started", "Starting notification decorator example program")
    
    try:
        # 1. Data processing example
        print("\n📊 Example 1: Data Processing")
        result1 = process_data(500)
        print(f"Result: {result1}")
        
        # 2. File upload example
        print("\n📁 Example 2: File Upload")
        result2 = upload_file("important_data.csv")
        print(f"Result: {result2}")
        
        # 3. Network request example (might fail)
        print("\n🌐 Example 3: Network Request")
        try:
            result3 = fetch_data()
            print(f"Result: {result3}")
        except Exception as e:
            print(f"Request failed: {e}")
        
        # 4. Model training example
        print("\n🤖 Example 4: Model Training")
        result4 = train_model()
        print(f"Result: {result4}")
        
        # 5. Batch processing example
        print("\n📦 Example 5: Batch Processing")
        result5 = batch_process()
        print(f"Result: {result5}")
        
        # Manual notifications with different types
        print("\n📱 Manual Notification Examples")
        notify("Info Notification", "This is a regular info notification", "completed")
        notify("Warning Notification", "This is a warning notification", "error")
        notify("Stop Notification", "This is a stop notification", "stopped")
        
        # Final success notification
        notify("Example Program Completed", "All examples executed successfully! Notification system working properly.")
        
    except Exception as e:
        # If there are uncaught errors, send error notification
        notify("Example Program Error", f"Error occurred during execution: {str(e)}", "error")
        raise
    
    print("\n✅ All examples completed!")
    print("📱 Please check your ntfy notifications!")

if __name__ == "__main__":
    main()
