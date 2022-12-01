number_of_data = 5
need_eeg_data = 10

total_data = {
    "Index":[],
    "EEG":[],
    "BIS":[],
    "Time":[]
}

for i in range(number_of_data):
    total_data["Index"].append(i)
    total_data["BIS"].append(i)
    total_data["Time"].append(f"{i}s")

for i in range(number_of_data+need_eeg_data):
    total_data["EEG"].append(i)

def print_look_good(data: total_data):
    print("Index\tEEG\tBIS\tTime")
    for i in range(number_of_data):
        for j in range(i,need_eeg_data+i):
            print()
            # other_index_1 = j//need_eeg_data
            # other_index_2 = j%need_eeg_data
            # if other_index_2 == 0:
            #     print(data["Index"][other_index_1],"\t",data["EEG"][j],"\t",data["BIS"][other_index_1],"\t",data["Time"][other_index_1])
            # elif other_index_2 < need_eeg_data-1:
            #     print(data["Index"][other_index_1],"\t",data["EEG"][j],"\t\t")
            # elif other_index_2 == need_eeg_data-1:
            #     break
            # print(data["Index"][i],"\t",data["EEG"][i],"\t",data["BIS"][i],"\t",data["Time"][i])
    
print_look_good(total_data)