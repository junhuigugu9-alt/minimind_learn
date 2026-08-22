# RMSNorm

## torch.nn.Module作用
torch.nnModule是RMSNorm的基类（Base Class）。是pytorch所有神经网络模块的父类。继承该父类的类，可以利用pytorch内置机制自动维护参数列表和移动数据。  

## x.float()和.type_as(x)
防止FP16（16位浮点数，Half Precision Floating Point，半精度浮点数）下计算溢出。  
1. x.float()
    - 作用：强制将输入张量从FP16（半精度）或BF16提升为FP32（单精度）。
2. .type_as(x)
    - 作用：将.前的张量数值类型变为与x相同的类型。
- 两者合用的效果：既保证了数值稳定性，又保留了低精度带来的显存节省和带宽加速。

## 满足什么条件的张量在模型训练时能被更新？
1. 张量的 .requres_grad=True。
2. 该张量被传入优化器的构造函数中。

**nn.Parameter**的作用: 可以让 model.parameters() 迭代器自动捕获 nn.Parameter 类型的变量。能够和其他组件中的参数统一传给优化器用于训练时权重更新。