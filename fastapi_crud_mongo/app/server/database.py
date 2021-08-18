from motor import motor_asyncio
from bson.objectid import ObjectId


MONGO_DETAILS = "mongodb://127.0.0.1:21017"

client = motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.students

student_collection = database.get_collection("student_collection")



# Helpers
def student_helper(student) -> dict:
    """(Helper function)
    
        To format student data
    """
    return {
        "id": str(student["_id"]),
        "name": student["name"],
        "email": student["email"],
        "course_of_study": student["course_of_study"],
        "year": student["year"],
        "gpa": student["gpa"]
    }

async def retrieve_students():
    """Retrieve data of all students"""
    students = []
    async for student in student_collection.find():
        students.append(student_helper(student))
    return students

async def add_student(student_data: dict) -> dict:
    """Add student data for one student"""
    student = await student_collection.insert_one(student_data)
    new_student = await student_collection.find_one({"_id": student.inserted_id})

    return student_helper(new_student)


async def retrieve_student(id: str) -> dict:
    """Retrieve data for one student"""
    student = await student_collection.find_one({"_id": ObjectId(id)})
    if student:
        return student_helper(student)

async def update_student(id: str, data:dict):
    """Update data for one student"""
    if len(data) < 1:
        return False
    student = await student_collection.find_one({"_id": ObjectId(id)})
    if student:
        update_student = await student_collection.update_one(
            {
                "_id": ObjectId(id),
                "$set": data
            }
        )

        if update_student:
            return True
        return False

async def delete_student(id: str):
    """Delete a student from the database"""
    student = await student_collection.find_one({"_id": ObjectId(id)})
    if student:
        await student_collection.delete_one({"_id": ObjectId(id)})
        return True