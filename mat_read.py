# read the file named abc.mat
import scipy.io as scio

file = '/Users/xuepenghui/PycharmProjects/practice/abc.mat'
data = scio.loadmat(file)
sample = data['persons']
# print(sample)
# print(type(sample))
# print(sample[0])
# print(sample[0][0])
# print(sample[0][0][0])
# print(sample[0][0][0][0])
# for i in range(101):
#   print(sample[0][i][379][0])


train_data = []
for i in range(101):
    temp = []
    for j in range(380):
        temp.append(sample[0][i][j])
    train_data.append(temp)
