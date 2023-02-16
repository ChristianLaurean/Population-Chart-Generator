import matplotlib.pyplot as plt

def generate_bar_chart(labels, values,country):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.savefig(f'./imgs/{country}.png')
    plt.close()

def generate_pie_chart(labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    ax.axis('equal')
    plt.savefig('./imgs/' + 'countries with the largest population.png')
    plt.close()


if __name__ == '__main__':
    generate_bar_chart()
