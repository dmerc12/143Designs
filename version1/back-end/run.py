from API import create_back_end_api
from Database import DBConnection

app = create_back_end_api(DBConnection)

if __name__ == "__main__":
    app.run(debug=True)
