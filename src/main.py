from textnode import *
import os
import shutil

def main():
    this_location = os.path.abspath(__file__)
    this_dir = os.path.dirname(__file__)
    destination = os.path.normpath(os.path.join(this_dir,"..","public"))
    source_location = os.path.normpath(os.path.join(this_dir, "..", "static"))
    deletion_location = os.path.normpath(os.path.join(this_dir, "..", "test"))
    from_here = os.path.normpath(os.path.join(this_dir, "..", "from_here"))
    to_here = os.path.normpath(os.path.join(this_dir, "..", "to_here")) 

    """
    For the sake of testing this section is just made to build out the test locations
    """
    def test_setup(from_here, deletion_location, to_here):
        try:
            if not os.path.exists(from_here):
                os.makedirs(from_here)
            
            if not os.path.exists(deletion_location):
                os.makedirs(deletion_location)

            if not os.path.exists(to_here):
                os.makedirs(to_here)
            
            with open(os.path.join(from_here, "t1.py"),"w") as f:
                pass
            with open(os.path.join(from_here, "t2.py"),"w") as f:
                pass
        except Exception as e:
            print(e)
            exit()

    test_setup(from_here, deletion_location, to_here)
    """
    End of test setup section. Delete when this is done.
    """      

    # Delete old destination
    shutil.rmtree(deletion_location)        # Deletion works
    # Copy everything from the source location
    for item in os.listdir(from_here):
        source_path = os.path.join(from_here, item)
        destination_path = os.path.join(to_here, item)
        if os.path.isfile(source_path):
            shutil.copy(source_path, destination_path)
            print(f"Copied file: {source_path} and moved to {destination_path}")
        elif os.path.isdir(source_location):
            shutil.copytree(source_path, destination_path)
            print(f"Copied dir: {source_path} and moved to {destination_path}")
    print(f"Everything from {source_path} has been copied to {destination_path}")

if __name__ == "__main__":
    main()