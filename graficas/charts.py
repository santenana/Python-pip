import matplotlib.pyplot as plt

def pie_chart():
    labels = ['A','B','C']
    valores = [200,36,120]

    fig,ax = plt.subplots()
    ax.pie(valores,labels=labels)
    plt.savefig('pie.png')
    plt.close()
