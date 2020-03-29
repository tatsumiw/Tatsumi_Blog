### get请求和post请求：
1. get请求：
    * 使用场景：如果只对服务器获取数据，并没有对服务器产生任何影响，那么这时候使用get请求。
    * 传参：get请求传参是放在url中，并且是通过`?`的形式来指定key和value的。
2. post请求：
    * 使用场景：如果要对服务器产生影响，那么使用post请求。
    * 传参：post请求传参不是放在url中，是通过`form data`的形式发送给服务器的。

### get和post请求获取参数：
1. get请求是通过`flask.request.args`来获取。
2. post请求是通过`flask.request.form`来获取。
3. post请求在模板中要注意几点：
    * input标签中，要写name来标识这个value的key，方便后台获取。
    * 在写form表单的时候，要指定`method='post'`，并且要指定`action='/login/'`。
4. 示例代码：
    ```
        <form action="{{ url_for('login') }}" method="post">
            <table>
                <tbody>
                    <tr>
                        <td>用户名：</td>
                        <td><input type="text" placeholder="请输入用户名" name="username"></td>
                    </tr>
                    <tr>
                        <td>密码：</td>
                        <td><input type="text" placeholder="请输入密码" name="password"></td>
                    </tr>
                    <tr>
                        <td></td>
                        <td><input type="submit" value="登录"></td>
                    </tr>
                </tbody>
            </table>
        </form>
    ```

### 保存全局变量的g属性：
g：global
1. g对象是专门用来保存用户的数据的。
2. g对象在一次请求中的所有的代码的地方，都是可以使用的。

### 钩子函数（hook）：
1. before_request：
    * 在请求之前执行的
    * 是在视图函数执行之前执行的
    * 这个函数只是一个装饰器，他可以把需要设置为钩子函数的代码放到视图函数执行之前来执行
2. context_processor：
    * 上下文处理器应该返回一个字典。字典中的`key`会被模板中当成变量来渲染。
    * 上下文处理器中返回的字典，在所有页面中都是可用的。
    * 被这个装饰器修饰的钩子函数，必须要返回一个字典，即使为空也要返回。


