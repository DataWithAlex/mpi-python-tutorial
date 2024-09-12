# MPI with Python

This repository demonstrates the use of Message Passing Interface (MPI) in Python using `mpi4py`. It contains Python scripts that illustrate basic point-to-point communication and environment setup for parallel computing.

## Repository Structure

- **`point-to-point.py`**: A Python script demonstrating point-to-point communication between two MPI processes. Process 0 sends a "Hello, world" message to Process 1, which receives and prints it. The script includes explanatory print statements to guide you through each step of the communication process.

- **`mpi_test.py`**: A basic Python script that initializes an MPI communicator and prints a message from each process. It demonstrates how to initialize MPI in Python and verify that multiple processes are running.

- **`core_count.py`**: A simple Python script that prints the number of logical cores available on your system. This helps in understanding the number of processes you could potentially run in parallel.

## Installation

To run these scripts, you need to have Python, `mpi4py`, and an MPI implementation (such as Open MPI) installed on your system. Follow the instructions below to set up your environment.

### Step 1: Install Python and Create a Virtual Environment

Ensure you have Python 3 installed. Then, create a virtual environment to manage your dependencies:

```bash
python3 -m venv myenv
source myenv/bin/activate
```

### Step 2: Install mpi4py
With the virtual environment activated, install mpi4py:

```bash
pip install mpi4py
```

### Step 3: Install Open MPI

On macOS, you can install Open MPI using Homebrew:


```bash
brew install open-mpi
```

Configure Open MPI to use TCP for communication by setting the following environment variable:

```bash
export OMPI_MCA_btl="self,tcp"
```

Step 4: Install Dependencies from `requirements.txt`

```bash
pip install -r requirements.txt
```

# Running the Scripts

Running `point-to-point.py`

To run the point-to-point.py script, use the following command to start two MPI processes:

```bash
mpiexec -n 2 python3 point-to-point.py
```

### Expected Output

```bash
MPI communicator initialized.
Total number of processes: 2
This process has rank (ID): 0
Process 0 is sending the message: 'Hello, world' to process 1
Process 0 has sent the message to process 1.
MPI communicator initialized.
Total number of processes: 2
This process has rank (ID): 1
Process 1 is waiting to receive a message from process 0.
Process 1 received the message: 'Hello, world' from process 0.
```

## Running `mpi_test.py`

To run the `mpi_test.py` script, which prints messages from each process:

```bash
mpiexec -n 4 python3 mpi_test.py
```

### Expected Output

```bash
Hello from process 0
Hello from process 1
Hello from process 2
Hello from process 3
```

## Running `core_count.py`
To check the number of logical cores available on your system:

```bash
python3 core_count.py
```

Expected output:

```bash
Logical cores: 10
```