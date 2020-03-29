### cookie：
1. `cookie`出现的原因：在网站中，http请求是无状态的。也就是说即使第一次和服务器连接后并且登录成功后，第二次请求服务器依然不能知道当前请求是哪个用户。cookie的出现就是为了解决这个问题，第一次登录后服务器返回一些数据（cookie）给浏览器，然后浏览器保存在本地，当该用户发送第二次请求的时候，就会自动的把上次请求存储的cookie数据自动的携带给服务器，服务器通过浏览器携带的数据就能判断当前用户是哪个了。
2. 如果服务器返回了`cookie`给浏览器，那么浏览器下次再请求相同的服务器的时候，就会自动的把`cookie`发送给浏览器，这个过程，用户根本不需要管。
3. `cookie`是保存在浏览器中的，相对的是浏览器。

### session：
1. `session`介绍：session和cookie的作用有点类似，都是为了存储用户相关的信息。不同的是，cookie是存储在本地浏览器，而session存储在服务器。存储在服务器的数据会更加的安全，不容易被窃取。但存储在服务器也有一定的弊端，就是会占用服务器的资源，但现在服务器已经发展至今，一些session信息还是绰绰有余的。
2. 使用`session`的好处：
    * 敏感数据不是直接发送回给浏览器，而是发送回一个`session_id`，服务器将`session_id`和敏感数据做一个映射存储在`session`(在服务器上面)中，更加安全。
    * `session`可以设置过期时间，也从另外一方面，保证了用户的账号安全。

### flask中的session工作机制：
1. flask中的session机制是：把敏感数据经过加密后放入`session`中，然后再把`session`存放到`cookie`中，下次请求的时候，再从浏览器发送过来的`cookie`中读取`session`，然后再从`session`中读取敏感数据，并进行解密，获取最终的用户数据。
2. flask的这种`session`机制，可以节省服务器的开销，因为把所有的信息都存储到了客户端（浏览器）。
3. 安全是相对的，把`session`放到`cookie`中，经过加密，也是比较安全的，这点大家放心使用就可以了。

### 操作session：
1. session的操作方式：
    * 使用`session`需要从`flask`中导入`session`，以后所有和`sessoin`相关的操作都是通过这个变量来的。
    * 使用`session`需要设置`SECRET_KEY`，用来作为加密用的。并且这个`SECRET_KEY`如果每次服务器启动后都变化的话，那么之前的`session`就不能再通过当前这个`SECRET_KEY`进行解密了。
    * 操作`session`的时候，跟操作字典是一样的。
    * 添加`session`：`session['username']`。
    * 删除：`session.pop('username')`或者`del session['username']`。
    * 清除所有`session`：`session.clear()`
    * 获取`session`：`session.get('username')`
2. 设置session的过期时间：
    * 如果没有指定session的过期时间，那么默认是浏览器关闭后就自动结束
    * 如果设置了session的permanent属性为True，那么过期时间是31天。
    * 可以通过给`app.config`设置`PERMANENT_SESSION_LIFETIME`来更改过期时间，这个值的数据类型是`datetime.timedelay`类型。

