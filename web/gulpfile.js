'use strict';
    //gulp
var gulp        = require('gulp'),
    //多浏览器多设备同步&自动刷新
    browserSync = require('browser-sync').create(),
    SSI         = require('browsersync-ssi'),
    //压缩js
    //minify      = require('gulp-minify'),
    //错误处理插件plumber
    plumber     = require('gulp-plumber'),
    //compass 用来编译sass
    compass     = require('gulp-compass'),
    //clean 用来删除文件
    clean       = require('gulp-clean'),
    //压缩文件
    zip         = require('gulp-zip'),
    //控制task中的串行和并行
    runSequence = require('gulp-run-sequence');

//serve任务：监听所有文件夹，如果有文件变动，则重新编译并刷新浏览器
gulp.task('serve', function() {

    browserSync.init({
        server: {
            baseDir:["./dist"],
            //index:'templates/index.html',
            middleware:SSI({
                baseDir:'./dist',
                //index:'templates/index.html',
                ext:'.shtml',
                version:'2.14.0'
            })
        }
    });
    //监听各个目录的文件，如果有变动则执行相应的任务
    gulp.watch("app/sass/**/*.scss", ['compass']);
    gulp.watch("app/js/**/*.js", ['js']);
    gulp.watch("app/images/**/*", ['image']);
    gulp.watch("app/css/**/*", ['css']);
    gulp.watch("app/fonts/**/*", ['font']);
    gulp.watch("app/**/*.html", ['html']);
    gulp.watch("dist/templates/**/*.html").on("change",browserSync.reload);
});



//compass任务，将scss编译为css
gulp.task('compass', function() {
  return gulp.src('app/sass/**/*.scss')
        .pipe(compass({
          //设置生成sourcemap，在调试器中显示样式在scss文件中的位置，便于调试
          sourcemap: 'true',
          //输出格式设置为compressed就不需要压缩css了（nested, expanded, compact, or compressed.）
          style: 'compact',
          //文件目录
          css: 'dist/static/css',
          sass: 'app/sass',
          //image: 'app/images'
        }))
        .on('error', function(error) {
          // Would like to catch the error here
          console.log(error);
          this.emit('end');
        })
        .pipe(gulp.dest('dist/static/css'))
        .pipe(browserSync.stream());
});


//js任务，将js压缩后放入dist。该任务要在clean-scripts任务完成后再执行
gulp.task('js', function(){
    return gulp.src('app/js/**/*.js')
        .pipe(plumber())
        //目前没用混淆，不方便调试
        //.pipe(uglify())    
        //.pipe(minify())
        .pipe(gulp.dest("dist/static/js"))
        .pipe(browserSync.stream());
});

//image任务，复制图片过去
gulp.task('image', function() {
    return gulp.src("app/img/**/*")
        .pipe(plumber())        
        .pipe(gulp.dest("dist/static/img"))
        .pipe(browserSync.stream());
});

//css任务，复制外部引入的过去
gulp.task('css', function() {
    return gulp.src("app/css/**/*")
        .pipe(plumber())        
        .pipe(gulp.dest("dist/static/css"))
        .pipe(browserSync.stream());
});

//font任务，复制字体过去
gulp.task('font', function() {
    return gulp.src("app/fonts/**/*")
        .pipe(plumber())        
        .pipe(gulp.dest("dist/static/fonts"))
        .pipe(browserSync.stream());
});

//html任务，目前什么都没做
gulp.task('html', function() {
    gulp.src("app/index.html").pipe(plumber()).pipe(gulp.dest("dist/"));
    return gulp.src("app/*.html")
        .pipe(plumber())        
        .pipe(gulp.dest("dist/"))
        .pipe(browserSync.stream());
});

//clean任务：给下边的redist用,清空dist文件夹
gulp.task('clean', function () {
  return gulp.src('dist/*', {read: false})
    .pipe(clean());
});

//redist任务：需要时手动执行,先执行clean，然后再重建dist
gulp.task('redist',function(){
    //先运行clean，然后并行运行html,js,compass
    runSequence('clean',['html','js','compass','image','css','font']);
});

//运行gulp
gulp.task('default',function(){
    //先运行redist，启动服务器
    runSequence('redist','serve');
});

//publish任务，要手动执行，将dist中的文件分发到项目中的templates和static文件夹中。
gulp.task('publish', function(){
    gulp.src('dist/*.html').pipe(plumber()).pipe(gulp.dest('../templates'));
    gulp.src('dist/static/js/**/*.js').pipe(plumber()).pipe(gulp.dest('../static/js'));
    gulp.src('dist/static/css/**/*.css').pipe(plumber()).pipe(gulp.dest('../static/css'));
    gulp.src('dist/static/img/**/*').pipe(plumber()).pipe(gulp.dest('../static/img'));
    gulp.src('dist/static/fonts/**/*').pipe(plumber()).pipe(gulp.dest('../static/fonts'));
});

