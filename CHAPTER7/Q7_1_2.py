def list_averge(x):
    try:
        return sum(x)/len(x)
    except:
        print('list_length:', len(x))
        return None

print(list_averge([3.9, 4.5, 2.3]))
print(list_averge([]))
