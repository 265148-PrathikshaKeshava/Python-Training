import pickle
 
class Storage:
    #Saving in Pickle file
    @staticmethod
    def save_to_file(data, filename=r"C:\Users\265148\Desktop\New folder\Hackathon03\employe_mgmt\employees.pkl"):
        with open(filename, "wb") as file:
            pickle.dump(data, file)
        print(f"Saved the data to {filename} successfully.")
    
    #loading data from Pickle file
    @staticmethod
    def load_from_file(filename=r"C:\Users\265148\Desktop\New folder\Hackathon03\employe_mgmt\employees.pkl"):
        try:
            with open(filename, "rb") as file:
                return pickle.load(file)
        except FileNotFoundError:
            print(f"Can't find the file {filename}.")
            return []
 
 