matplotlib的一些用法
前置部分：图像映射颜色会因为设置不同而不同 常用8位灰度图（即2^8=256 从0-255） 不过科研与医学图像常用16位65536
            可以使用vmin和vmax来做设置
            不设置默认为数据中的max与min
    
    plt.figure
    新建画布

    plt.title('id')
    命名用的

    plt.colorbar
    颜色条 显示色块对应数字关系

    plt.tight_layout
    自动调整图像间隔关系 避免重合

    plt.imshow(#某个二维数组,cmap=##)
    其中##部分可用 ： 'gray' o=黑 ；其他=白
                    'gray_r' 即颜色反转
                    不写cmap默认彩色
    cmap后可使用插值-interpolation  具体用什么我也不知道   反正nearest是不插
        一般在后面加上vmax和vmin的设置

    plt.savefig('文件名'.png)

    plt.subplot(行数，列数，接下来使用的位置）
                                    位置的数法是：左到右 上到下
    