from mpi4py import MPI

# Initialize the MPI communicator
comm = MPI.COMM_WORLD
print("MPI communicator initialized.")

# Get the total number of processes involved
size = comm.Get_size()
print(f"Total number of processes: {size}")

# Get the rank (ID) of the current process
rank = comm.Get_rank()
print(f"This process has rank (ID): {rank}")

# Check if the current process is the sender (rank 0)
if rank == 0:
    # Prepare a message to send
    msg = "Hello, world"
    print(f"Process {rank} is sending the message: '{msg}' to process 1")

    # Send the message to process 1
    comm.send(msg, dest=1)
    print(f"Process {rank} has sent the message to process 1.")

# Check if the current process is the receiver (rank 1)
elif rank == 1:
    print(f"Process {rank} is waiting to receive a message from process 0.")

    # Receive the message from process 0
    s = comm.recv()
    print(f"Process {rank} received the message: '{s}' from process 0.")