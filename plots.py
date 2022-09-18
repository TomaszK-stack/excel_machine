import matplotlib.pyplot as plt
import xlwings as xw

@xw.func
def myplot(n, caller):
    fig = plt.figure()
    plt.plot(range(int(n)))
    caller.pictures.add(fig, name='MyPlot', update=True)
    return 'Plotted with n={}'.format(n)


