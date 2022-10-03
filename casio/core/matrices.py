
class NdArray:
    def __init__(self, value, dims=None):
        self.value = []
        for i in range(len(dims)):
            dim = dims[i]
            for j in range(dim):

            self.value.append([])
            for j in range(dims[i]):
                self.value[i].append(value)
