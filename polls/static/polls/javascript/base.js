
$(document).ready( function() {

  var isHovered;
  var isHoveredLi;
  var bool;

  $(".nav-product").hover(function (event) {
    if (bool) {
      $(".desktop_menu_products").fadeIn(0);
      bool = false;
    }
      $(".desktop_menu_products").fadeIn(100);
  }, function(){
      isHovered = $('.desktop_menu_products').is(".desktop_menu_products:hover"); // returns true or false
      if (isHovered === false) {
        $(".desktop_menu_products").fadeOut();
      }
  });
  $(".desktop_menu_products").hover(function (event) {
      $(this).fadeIn(0);
  }, function(){
      isHoveredLi = $('.nav-product-a').is(".nav-product-a:hover"); // returns true or false
      if (isHoveredLi) {
        $(this).fadeOut(0);
        bool = true;
      }
      else {
        $(this).fadeOut();
      }
  });

  $(".nav-case").hover(function (event) {
    if (bool) {
      $(".desktop_menu_case").fadeIn(0);
      bool = false;
    }
      $(".desktop_menu_case").fadeIn(100);
  }, function(){
      isHovered = $('.desktop_menu_case').is(".desktop_menu_case:hover"); // returns true or false
      if (isHovered === false) {
        $(".desktop_menu_case").fadeOut();
      }
  });
  $(".desktop_menu_case").hover(function (event) {
      $(this).fadeIn(0);
  }, function(){
      isHoveredLi = $('.nav-case-a').is(".nav-case-a:hover"); // returns true or false
      if (isHoveredLi) {
        $(this).fadeOut(0);
        bool = true;
      }
      else {
        $(this).fadeOut();
      }
  });

    $(".nav-about").hover(function (event) {
      if (bool) {
        $(".desktop_menu_about").fadeIn(0);
        bool = false;
      }
        $(".desktop_menu_about").fadeIn(100);

    }, function(){
        isHovered = $('.desktop_menu_about').is(".desktop_menu_about:hover"); // returns true or false
        if (isHovered === false) {
          $(".desktop_menu_about").fadeOut();
        }
    });
    $(".desktop_menu_about").hover(function (event) {
        $(this).fadeIn(0);
    }, function(){
        isHoveredLi = $('.nav-about-a').is(".nav-about-a:hover"); // returns true or false
        if (isHoveredLi) {
          $(this).fadeOut(0);
          bool = true;
        }
        else {
          $(this).fadeOut();
        }
    });

      $(".nav-contact").hover(function (event) {
        if (bool) {
          $(".desktop_menu_contact").fadeIn(0);
          bool = false;
        }
          $(".desktop_menu_contact").fadeIn(100);

      }, function(){
          isHovered = $('.desktop_menu_contact').is(".desktop_menu_contact:hover"); // returns true or false
          if (isHovered === false) {
            $(".desktop_menu_contact").fadeOut();
          }
      });
      $(".desktop_menu_contact").hover(function (event) {
          $(this).fadeIn(0);
      }, function(){
          isHoveredLi = $('.nav-contact-a').is(".nav-contact-a:hover"); // returns true or false
          if (isHoveredLi) {
            $(this).fadeOut(0);
            bool = true;
          }
          else {
            $(this).fadeOut();
          }
      });
});
