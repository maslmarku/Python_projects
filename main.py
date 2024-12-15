from fastapi import FastAPI
app = FastAPI()

# Define a function to return a description of the app
def get_app_description():
	return (
    	"Welcome to the Iris Species Prediction API!"
    	"This API allows you to predict the species of an iris flower based on its sepal and petal measurements."
    	"Use the '/predict/' endpoint with a POST request to make predictions."
    	"Example usage: POST to '/predict/' with JSON data containing sepal_length, sepal_width, petal_length, and petal_width."
	)

def testado(name):
    return (
    	{"my teste" + name}
	)

def adduser(id):
	global newid
	newid+=id
	return ({"my teste" : newid})


# Define the root endpoint to return the app description
@app.get("/")
async def root():
	return {"message": get_app_description()}
@app.get("/teste")
async def hello(name: str):
	return {"message": testado(name)}

@app.put("/adduser")
async def addu(int: id):
	return {"message": adduser(id)}
