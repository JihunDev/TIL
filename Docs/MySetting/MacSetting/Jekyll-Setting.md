# Jekyll Setting

[jekyll Home Page](https://jekyllrb-ko.github.io)



## install

```shell
$ sudo gem install bundler jekyll
```



## Getting Start

```shell
$ bundle exec Jekyll serve
```



Server Address : http://127.0.0.1:4000



## Troubleshooting

### Err

```shell
$ bundle exec jekyll serve                                                                                           Could not find minitest-5.11.3 in any of the sources
Run `bundle install` to install missing gems.
```



### 해결

```shell
$ bundle install
```