$(document).ready(function() {
    // Función para validar el correo electrónico
    function isValidEmail(email) {
      var emailRegex = /\S+@\S+\.\S+/;
      return emailRegex.test(email);
    }
  
    // Función para validar el formulario
    function validateForm() {
      var emailInput = $("#email");
      var nameInput = $("#name");
      var phoneInput = $("#phone");
      var addressInput = $("#address");
      var passwordInput = $("#password");
  
      // Validar correo electrónico
      if (!isValidEmail(emailInput.val())) {
        emailInput.addClass("is-invalid");
        return false;
      } else {
        emailInput.removeClass("is-invalid");
      }
  
      // Validar campos vacíos
      if (nameInput.val() === "" || phoneInput.val() === "" || addressInput.val() === "") {
        nameInput.addClass("is-invalid");
        phoneInput.addClass("is-invalid");
        addressInput.addClass("is-invalid");
        passwordInput.addClass("is-invalid");
        return false;
      } else {
        nameInput.removeClass("is-invalid");
        phoneInput.removeClass("is-invalid");
        addressInput.removeClass("is-invalid");
        passwordInput.removeClass("is-invalid");
      }
  
      return true;
    }
  
    // Agregar evento de envío de formulario
    $("#contact-form").submit(function(event) {
      if (!validateForm()) {
        event.preventDefault();
      }
    });
  });
  