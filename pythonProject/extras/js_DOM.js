document.addEventListener('readystatechange', function() {
    if (document.readyState === "complete") {
      console.log(" Javascript Connected !!")
      init();
    }
});

function init() {
    var headOne = document.getElementById("one");
    var headTwo = document.getElementById("two");
    var headThree = document.getElementById("three");

    headOne.addEventListener('mouseover', function(){
        headOne.innerHTML = "Mouse overing on h1";
        headOne.style.color = 'green';
    })
     headOne.addEventListener('mouseout', function(){
        headOne.innerHTML = "This is heading";
        headOne.style.color = 'blue';
    })
    headTwo.addEventListener('click', function(){
        headTwo.innerHTML = "Mouse clicked h2";
    })
    headTwo.addEventListener('dblclick', function(){
        headTwo.innerHTML = "Mouse double clicked h2";
    })
  }


///*
//> document.URL
//< "https://www.udemy.com/course/python-and-django-full-stack-web-developer-bootcamp/learn/lecture/6598240#notes"
//
//> document.body
//< <body id="udemy" class="udemy pageloaded">…</body>
//
//>  document.head
//< <head>…</head>
//
//> document.links
//< HTMLCollection [<a>, <a>, <a class="header--header-link--1gRxA header--course-title--tHmMe">, <a>, <a>, <a>, <a>, <a class="report-abuse-launcher--menu-link--2iEhR">, <a class="report-abuse-launcher--menu-link--2iEhR">, <a>, …] (42)
//
//> document.getElementById("singlep")
//< <p id="singlep">
//    single paragraph
//</p>
//
//> document.getElementsByClassName("firstdiv")
//< HTMLCollection [<div class="firstdiv">] (1)
//
//> document.querySelector("#singlep")
//< <p id="singlep">
//    single paragraph
//</p>
//
//> var p = document.querySelector("p")
//< undefined
//> p.textContent = "this is ne line"
//< "this is ne line"
//> p.innerHTML = "<strong>this is ne line</strong>"
//< "<strong>this is ne line</strong>"
//
//> var aa = document.querySelector("a")
//> a.getAttribute("href")
//< "https://www.amazon.com"
//> a.setAttribute("href", "https://www.google.com")*/
