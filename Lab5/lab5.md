# Lab 5

# Part 1

## Step 1 && Step 2
![Screenshot from 2019-06-21 11-20-52](https://user-images.githubusercontent.com/40375246/59935876-b6e58100-941c-11e9-94d6-3b56369f9350.png)
![Screenshot from 2019-06-21 11-20-24](https://user-images.githubusercontent.com/40375246/59935885-bc42cb80-941c-11e9-8314-cbd8302acdeb.png)

## Step 3
![Screenshot from 2019-06-21 11-44-24](https://user-images.githubusercontent.com/40375246/59935949-e2686b80-941c-11e9-91a1-89df67258c70.png)
![Screenshot from 2019-06-21 11-44-49](https://user-images.githubusercontent.com/40375246/59935955-e3999880-941c-11e9-9f5e-78e06c9d918b.png)

## Step 4
![Screenshot from 2019-06-21 11-50-32](https://user-images.githubusercontent.com/40375246/59935992-fca24980-941c-11e9-996e-5254e0367828.png)
![Screenshot from 2019-06-21 11-51-09](https://user-images.githubusercontent.com/40375246/59935996-fdd37680-941c-11e9-972d-9ab6baa1e1ee.png)

## Step 5
![Screenshot from 2019-06-21 12-21-49](https://user-images.githubusercontent.com/40375246/59936967-3d9b5d80-941f-11e9-968e-bcd8f25fa749.png)
![Screenshot from 2019-06-21 12-21-29](https://user-images.githubusercontent.com/40375246/59936971-3ecc8a80-941f-11e9-8161-5de39c1184d8.png)

# Part 2

Makefile
```
all: static
static: program.o libprint.a
	cc program.o libprint.a -o static
shared: program.o libblock.so
	cc program.o libblock.so -o shared -Wl,-rpath='.'

libprint.a: block.o
	ar qc libprint.a source/block.o
program.o:
	cc -fPIC -c program.c -o program.o
libblock.so: block.o
	cc -shared -o libblock.so source/block.o
clean:
	rm -f *.o Makefile.bak
block.o:
	cc -fPIC -c source/block.c -o source/block.o
```
CMakeLists
```
cmake_minimum_required(VERSION 3.10.2)
project(Dynamic)
add_library(SharedSource SHARED source/block.c)
add_library(StaticSource STATIC source/block.c)

add_executable(Shared program.c)
target_link_libraries(Shared SharedSource)

add_executable(Static program.c)
target_link_libraries(Static StaticSource)
```
