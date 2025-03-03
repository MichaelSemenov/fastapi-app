from create_fastAPI_app import create_app
from router import router as tasks_router

app = create_app(create_custom_static_urls=True)
app.include_router(tasks_router)
