def processUrl(url,taskID):
    try:
        task = UrlTask.objects.get(id=task_id)
        
        if response.status_code == 200:
            task.status = 'completed'
            task.result = response.json()  # Save the fetched data
        else:
            task.status = 'failed'
            task.result = {"error": "Failed to fetch data", "status_code": response.status_code}
    except Exception as e:
        task.status = 'failed'
        task.result = {"error": str(e)}
    finally:
        task.save()


# Wrapper function to run the task in a thread
def backgroundThread(url, task_id):
    thread = threading.Thread(target=processUrl, args=(url, task_id))
    thread.start()