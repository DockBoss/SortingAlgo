#Quick Sort
from tkinter import *
from tkinter import ttk
import random
import time

unsorted_list = []

#build array of random numbers
def random_list(length):
    
    for i in range(length):    
        unsorted_list.append(random.randint(0, 800))
    return unsorted_list



def draw_list(list, low, high, pivot_index):
    sort_view.delete("all")
    canvas_height = 950
    canvas_width = 1000
    block_width = canvas_width // (len(list) + 1)
    offset = 10
    space = 1
    for i, num in enumerate(list):
        
        x0 = i * block_width + offset + space
        y0 = canvas_height - num

        x1 = (i + 1) * block_width + offset
        y1 = canvas_height
        print(i, low, high, pivot_index)
        if i == low or i == high or i == pivot_index:
            sort_view.create_rectangle( x0, y0, x1, y1, fill= 'green')
        else:
            sort_view.create_rectangle( x0, y0, x1, y1, fill = 'white')
    app.update_idletasks()

def sort_list():
    
    unsorted_list = random_list(int(length_entry.get()))
    print(unsorted_list)
    draw_list(unsorted_list, 0, len(unsorted_list) -1, 1)

def start_sort():
    print(unsorted_list)
    quick_sort(unsorted_list,0 , len(unsorted_list) -1)
    draw_list(unsorted_list, 0, len(unsorted_list) -1, 1)
    print(unsorted_list)
    unsorted_list.clear()


def partition(arr: list, low: int, high: int):
    pivot = arr[high]
    pivot_index = low
    draw_list(arr, low, high, pivot_index)
    for i in range(low, high): 
      
        time.sleep(0.1)
        if pivot > arr[i]:
            swap = arr.pop(i)
            arr.insert(pivot_index, swap)
            pivot_index += 1
            
            draw_list(arr, low, high, pivot_index)
    arr.insert(pivot_index, arr.pop(high))
    return pivot_index

def quick_sort(arr: list, low: int, high: int):

    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)
    
        
        

app = Tk()
app.title("Quick Sort")
app.maxsize(1000,1000)


main_frame = Frame(app, width = 1000, height = 50)
main_frame.grid(column =0, row = 0)

sort_view = Canvas(app, width = 1000, height= 950, bg = "black")
sort_view.grid(row = 1, column = 0, sticky = W)

length_label = Label(main_frame, text="List Length", font =("bold", 14), width = 10)
length_label.grid(row= 0, column= 0, sticky = W)

length_text = StringVar()
length_entry = Entry(main_frame, textvariable= length_text)
length_entry.grid(row =0, column = 1, sticky = W)



sort_button = Button(main_frame, text="Sort", width = 12, command = sort_list)
sort_button.grid(row = 0, column = 3, padx= 20)



start_button = Button(main_frame, text="Start", width = 12, command = start_sort)
start_button.grid(row = 0, column = 4, padx= 20)

app.mainloop()

#run program



