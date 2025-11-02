# 1️⃣ Use an official lightweight Python image
FROM python:3.12-slim

# 2️⃣ Prevent Python from writing .pyc files and enable unbuffered logging
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 3️⃣ Set the working directory inside the container
WORKDIR /app

# 4️⃣ Copy dependency file first (for Docker layer caching)
COPY requirements.txt /app/

# 5️⃣ Install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# 6️⃣ Copy the rest of the project code
COPY . /app/

# 7️⃣ Expose the Django default port
EXPOSE 8000

# 8️⃣ Define entrypoint script (responsible for initializing the container)
ENTRYPOINT ["python3", "manage.py"]

# 9️⃣ CMD provides default arguments to the entrypoint
CMD ["runserver", "0.0.0.0:8000"]

