function validateForm(field)
    {

        if( field == "first_name" )
        {
            first_name= document.getElementById("first_name").value;
            reg_ex=/^[a-zA-Z]*$/

            if(first_name.length > 10 || reg_ex.test(first_name)!=1)
            {
                document.getElementById("f_name").innerHTML = '(Max 10 alphabets only.)';
                document.add_employee.first_name.focus()
            }
            else
            {
                document.getElementById("f_name").innerHTML = '';
            }
        }

        else if( field == "last_name" )
        {
            last_name= document.getElementById("last_name").value;
            reg_ex=/^[a-zA-Z]*$/

            if(last_name.length > 20 || reg_ex.test(last_name)!=1)
            {
                document.getElementById("l_name").innerHTML = '(Max 20 alphabets only.)';
                document.add_employee.last_name.focus()
            }
            else
            {
                document.getElementById("l_name").innerHTML = '';
            }
        }
        else if( field == "email" )
        {
            reg_ex=/^\w+([\.-]?\w+)*@exusia.com$/
            email=document.getElementById("email").value;

            if(reg_ex.test(email)!=1)
            {
                document.getElementById("msg_email").innerHTML = '(Please Enter valid email.)';
                document.add_employee.email.focus()
            }
            else
            {
                document.getElementById("msg_email").innerHTML = '';
            }
        }
        else if( field == "mob" )
        {
            reg_ex=/^[0-9]*$/
            mob=document.getElementById("mob").value;

            if(String(mob).length != 10 || reg_ex.test(mob)!=1)
            {
                document.getElementById("msg_mob").innerHTML = '(Please Enter valid 10 digit mobile number.)';
                document.add_employee.mob.focus()
            }
            else
            {
                document.getElementById("msg_mob").innerHTML = '';
            }
        }

        else if( field == "aadhar" )
        {
            reg_ex=/^[0-9]*$/
            aadhar=document.getElementById("aadhar_card").value;

            if(String(aadhar).length != 16 || reg_ex.test(aadhar)!=1 )
            {
                document.getElementById("msg_aadhar").innerHTML = '(Please Enter valid 16 digit aadhar number.)';
                document.add_employee.aadhar_card.focus()
            }
            else
            {
                document.getElementById("msg_aadhar").innerHTML = '';
            }
        }

        else if( field == "pwd" )
        {
            reg_ex=/(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#\$%\^&\*])(?=.{8,})/
            pwd=document.getElementById("pwd").value;

            if(pwd.length < 8 )
            {
                document.getElementById("msg_pwd").innerHTML = '(Password must be eight characters or longer.)';
                document.add_employee.pwd.focus()
            }
            else if( reg_ex.test(pwd)!=1 )
            {
                document.getElementById("msg_pwd").innerHTML = '(Password must contain at least 1 lowercase,1 uppercase,1 special character.)';
                document.add_employee.pwd.focus()
            }
            else
            {
                document.getElementById("msg_pwd").innerHTML = '';
            }
        }

    }