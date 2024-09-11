# Fibonacci Appliaction on Nada by Nillion
This app takes a number as index, and calculates and returns its value from Fibonacci sequence. for now max is limited to 100, so if given index is more, app returns 4 - which means out of range ( 4 - because it does not appear in Fibonacci sequence )

1. Install Nillion sdk 
```
curl https://nilup.nilogy.xyz/install.sh | bash
```
   Use nilup to install the latest version of the Nillion SDK.
```
nilup install latest
nilup use latest
nilup init
```
2. Clone this repo and go to folder
```
git clone https://github.com/CreeptoCat/nada_fibonacci
cd nada_fibonacci

```
3. Create venv, activate and install nada-dsl
```
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade nada-dsl
```
4. Run the nada build command to compile app

```
nada build
```
5. Run app with test values

First success_test - which will give a number from Fibonacci sequence

```
nada run success_test
```
Second max_out_test - where the number we give to app is more than 100 and it returns 4
```
nada run max_out_test
```
You can also change test yaml files in `tests` folder, to test with your values
