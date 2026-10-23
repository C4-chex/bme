# ============================================
# 用 PyTorch 实现一个完整的 CNN 图像分类器
# 包含卷积、池化、残差连接
# ============================================

import torch
import torch.nn as nn   #导入神经网络模块
import torch.nn.functional as F    #导入神经网络函数模块


class ResidualBlock(nn.Module):
    """一个简单的残差块"""

    def __init__(self, in_channels: int, out_channels: int, stride: int = 1):
        super().__init__() #初始化父类
        # 第一个卷积层
        self.conv1 = nn.Conv2d(
            in_channels, out_channels,
            kernel_size=3, stride=stride, padding=1, bias=False
        )
        self.bn1 = nn.BatchNorm2d(out_channels)

        # 第二个卷积层
        self.conv2 = nn.Conv2d(
            out_channels, out_channels,
            kernel_size=3, stride=1, padding=1, bias=False
        )
        self.bn2 = nn.BatchNorm2d(out_channels)

        # 快捷连接（用于匹配维度变化）
        self.shortcut = nn.Sequential()
        if stride != 1 or in_channels != out_channels:
            self.shortcut = nn.Sequential(
                nn.Conv2d(
                    in_channels, out_channels,
                    kernel_size=1, stride=stride, bias=False
                ),
                nn.BatchNorm2d(out_channels)
            )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        # 主路径：卷积 → BN → ReLU → 卷积 → BN
        out = F.relu(self.bn1(self.conv1(x)))
        out = self.bn2(self.conv2(out))

        # 残差连接：加上输入（或经过维度变换的输入）
        out += self.shortcut(x)

        # 最后的 ReLU
        out = F.relu(out)
        return out


class SimpleCNN(nn.Module):
    """用于图像分类的简单 CNN（带残差连接）"""

    def __init__(self, num_classes: int = 10):
        super().__init__()
        # 初始卷积层
        self.conv1 = nn.Conv2d(3, 32, kernel_size=3, stride=1, padding=1)
        self.bn1 = nn.BatchNorm2d(32)

        # 残差层
        self.layer1 = ResidualBlock(32, 32)
        self.layer2 = ResidualBlock(32, 64, stride=2)
        self.layer3 = ResidualBlock(64, 64)

        # 全局平均池化
        self.global_pool = nn.AdaptiveAvgPool2d((1, 1))

        # 分类头
        self.fc = nn.Linear(64, num_classes)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        # x 形状: (batch_size, 3, 32, 32)
        x = F.relu(self.bn1(self.conv1(x)))

        x = self.layer1(x)  # (batch_size, 32, 32, 32)
        x = self.layer2(x)  # (batch_size, 64, 16, 16)
        x = self.layer3(x)  # (batch_size, 64, 16, 16)

        x = self.global_pool(x)  # (batch_size, 64, 1, 1)
        x = x.view(x.size(0), -1)  # (batch_size, 64)
        x = self.fc(x)  # (batch_size, num_classes)

        return x


# 创建模型并测试
model = SimpleCNN(num_classes=10)
print("模型结构：")
print(model)

# 测试前向传播
# 创建一个假的 batch：4 张图片，每张 3×32×32（RGB 32×32）
test_input = torch.randn(4, 3, 32, 32)
test_output = model(test_input)
print(f"\n输入形状: {test_input.shape}")
print(f"输出形状: {test_output.shape} (batch_size, num_classes)")