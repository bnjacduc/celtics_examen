$(document).ready(function () {
  
  $("#date").datepicker();

  
  function isValidEmail(email) {
    var emailRegex = /\S+@\S+.\S+/;
    return emailRegex.test(email);
  }

  
  function validateForm() {
    var emailInput = $("#email");
    var nameInput = $("#name");
    var phoneInput = $("#phone");
    var dateInput = $("#date");

    
    if (!isValidEmail(emailInput.val())) {
      emailInput.addClass("is-invalid");
      return false;
    } else {
      emailInput.removeClass("is-invalid");
    }
    
    var phoneRegex = /^[0-9]+$/;
    if (!phoneRegex.test(phoneInput.val())) {
      phoneInput.addClass("is-invalid");
      return false;
    } else {
      phoneInput.removeClass("is-invalid");
    }

    
    if (
      nameInput.val() === "" ||
      phoneInput.val() === "" ||
      dateInput.val() === ""
    ) {
      nameInput.addClass("is-invalid");
      phoneInput.addClass("is-invalid");
      dateInput.addClass("is-invalid");
      return false;
    } else {
      nameInput.removeClass("is-invalid");
      phoneInput.removeClass("is-invalid");
      dateInput.removeClass("is-invalid");
    }

    return true;
  }

  
  $("#form-title").text("Compra de entradas");

  
  $("#contact-form").submit(function (event) {
    if (!validateForm()) {
      event.preventDefault();
    }
  });
});
