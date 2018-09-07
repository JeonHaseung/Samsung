$(function() {
    $('.mybut').click(function() {
      console.log($(this).val());
      var coin= $(this).val();
      
      var DATA = {"which" : coin,}
      document.getElementById("H1").innerHTML = coin + " Forecast";
        
        
      $.ajax({
        url: $('#coin_table').attr('url'),
        type: 'POST',
        data: DATA,
        success: function(result, textstatus, xhr) {
            
            var f1 = document.getElementById("five");
            f1.innerHTML = result.f1;
            if (result.f1c)
                f1.style.color = "red";
            else
                f1.style.color = "blue";
            
            var f2 = document.getElementById("ten");
            f2.innerHTML = result.f2;
            if (result.f2c)
                f2.style.color = "red";
            else
                f2.style.color = "blue";
            
            var f3 = document.getElementById("thity");
            f3.innerHTML = result.f3;
            if (result.f3c)
                f3.style.color = "red";
            else
                f3.style.color = "blue";
            
            
            var f4 = document.getElementById("sixty");
            f4.innerHTML = result.f4;
            if (result.f4c)
                f4.style.color = "red";
            else
                f4.style.color = "blue";
            
            var f5 = document.getElementById("twelve");
            f5.innerHTML = result.f5;
            if (result.f5c)
                f5.style.color = "red";
            else
                f5.style.color = "blue";
            
            var f6 = document.getElementById("twentyfour");
            f6.innerHTML = result.f6;
            if (result.f6c)
                f6.style.color = "red";
            else
                f6.style.color = "blue";
            
        },
        error: function(xhr, textstatus, error) {
            console.log(xhr);
            console.log(textstatus);
            console.log(error);
        },
      });
        
    });
    
    setInterval(function () {
      $.ajax({
        url: $('#menu').attr('url'),
        type: 'POST',
        success: function(result, textstatus, xhr) {
            document.getElementById("first").innerHTML = "1등 : " + result.first;
            document.getElementById("second").innerHTML = "2등 : " + result.second;
            document.getElementById("third").innerHTML = "3등 : " + result.third;
        },
        error: function(xhr, textstatus, error) {
            console.log(xhr);
            console.log(textstatus);
            console.log(error);
        },
      });
    }
    ,3000);
    
    document.getElementById('LTC').click();
});