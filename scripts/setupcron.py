
import httpx



from langgraph_sdk import get_client
import asyncio
import uuid

# Initialize LangGraph client
client = get_client(url="http://127.0.0.1:8000")  # Ensure this is correct

async def create_thread():
    """Creates a thread and returns its ID."""
    try:
        thread_id = str(uuid.uuid4())  # Generate a new unique thread ID
        thread_info = await client.threads.create(thread_id=thread_id)
        print(f"✅ Thread created: {thread_info}")
        return thread_id
    except Exception as e:
        print(f"❌ Error creating thread: {str(e)}")
        return None

async def list_cron_jobs():
    """Lists all active cron jobs."""
    try:
        cron_jobs = await client.crons.search(
                assistant_id="6afd5261-8795-5804-a372-a182d3abfdd1",
                thread_id="36dcf922-ba8b-4301-8908-54497c872d59",
                limit=5,
                offset=5,
            )
        print(cron_jobs)
    except Exception as e:
        print(f"❌ Error fetching cron jobs: {str(e)}")
        
        
async def register_cron():
    """Registers a cron job on a thread."""
    thread_id = await create_thread()  # Get a thread ID

    if not thread_id:
        print("❌ No thread created. Cron job cannot be scheduled.")
        return

    try:
        cron_job =await client.runs.create(
            thread_id,
            "main",
            input={"email": ""},
            multitask_strategy="rollback",
        )
      
        print(f"✅ Cron job scheduled: {cron_job}")
    except Exception as e:
        print(f"❌ Error scheduling cron job: {str(e)}")

# Run the setup
if __name__ == "__main__":
    asyncio.run(list_cron_jobs())
