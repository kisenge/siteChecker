# Assuming the function is in utils.py
from ...processUrl import processData
import threading
from .models import UrlTask

def processUrl(url,taskId):
        # Call the data function
        data = processData(url)
        task = UrlTask.objects.get(id=taskId)

        # Process the data and update task status accordingly
        task.status = 'completed'
        task.result = data  # Store the processed data
    except Exception as e:
        task.status = 'failed'
        task.result = {"error": str(e)}
    finally:
        task.save()

# Wrapper function to run the task in a thread
def backgroundThread(url, task_id):
    thread = threading.Thread(target=processUrl, args=(url, task_id))
    thread.start()