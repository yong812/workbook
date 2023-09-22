
# 用户切换
su -
# 是否带‘-’号，切换用户身份的同时，是否切换当前使用的环境变量，环境变量是用来定义操作系统环境。

# 搜索
grep 
grep [options] pattern [files]
grep -n 搜索行，且显示行号
     -v 搜索不包含的行
     -i 忽略大小写
     -c 显示搜索到的次数
# 能够快速搜索文件中符合特定搜索模式的文本行，搜索文件，搜索目录均可。

# 创建文件，查看文件的内容
cat
cat options files
cat>new_file.txt            新建txt文件 （ctrl D 保存退出）
cat new_file.txt            显示单个文件内容
cat n1.txt n2.txt n3.txt    显示多个文件内容
cat a.txt>b.txt             将a文件内容拷贝到b文件（也可拷贝多个文件内容）
cat a.txt>>b.txt            将a文件内容添加到b文件末尾
tac a.txt                   按相反顺序显示文件内容
cat -n a.txt                在输出内容中使用行号
# 

可恶啊！！！







