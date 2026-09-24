matplotlib的一些用法
前置部分：图像映射颜色会因为设置不同而不同 常用8位灰度图（即2^8=256 从0-255） 不过科研与医学图像常用16位
            可以使用vmin和vmax来做设置
            不设置默认为数据中的max与min
    
    plt.figure
    新建画布


    plt.imshow(#某个二维数组,cmap=##)
    其中##部分可用 ： 'gray' o=黑 ；其他=白
                    'gray_r' 即颜色反转
                    不写cmap默认彩色
    cmap后可使用插值-interpolation  具体用什么我也不知道   反正nearest是不插

    plt.savefig('文件名'.png)