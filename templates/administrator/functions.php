<?php


class DB{
    private $host;
    private $username;
    private $password;
    private $financial_db;
    private $sotf_db;
    
    function set_finacial(){
        $this->host = "localhost";
        $this->username = "bets_admin";
        $this->password = "@saj9812223294";
        $this->financial_db = "bets_meftah1_financial";
    }
    
    function set_soft(){
        $this->host = "localhost";
        $this->username = "bets_admin";
        $this->password = "@saj9812223294";
        $this->sotf_db = "bets_meftah1";
    }
    
    
    function connect_financial(){
        $this->set_finacial();
        $host = $this->host;
        $username = $this->username;
        $password = $this->password;
        $db = $this->financial_db;
        
        $conn = new mysqli($host, $username, $password, $db);
        
        if ($conn->connect_error) {
            return(0);//failed
        }else{
            return($conn);//success
        }
    }
    
    
    function connect_soft(){
        $this->set_soft();
        $host = $this->host;
        $username = $this->username;
        $password = $this->password;
        $db = $this->sotf_db;
        
        $conn = new mysqli($host, $username, $password, $db);
        
        if ($conn->connect_error) {
            return(0);//failed
        }else{
            return($conn);//success
        }
    }
    
    
    function close($conn){
        $conn->close();
    }
}

class Student{
    
    function save_student($id_no, $name, $contact){
        // Create connection
        $db = new DB;
        $conn = $db->connect_financial();
        // Check connection
        if ($conn == 0) {
            return(101);
        }else{
            // Connected Successfuly!
            $douplicate = "SELECT id_no FROM student WHERE id_no='$id_no'";
            $result = $conn->query($douplicate);
            if ($result->num_rows > 0) {
                // Douplicated Record!
                return(102);
            } else {
                //every thing is okay!
                $save_student = "INSERT INTO student(id_no, name, contact)VALUES ('$id_no', '$name', '$contact')";
                if ($conn->query($save_student) === TRUE) {
                  return(1);// New record created successfully!
                } else {
                  return(103);// Probmel in isertion!
                }
                
            }
        }
        
    }
    
    function see_soft_student(){
        // Create connection
        $db = new DB;
        $conn = $db->connect_soft();
        // Check connection
        if ($conn == 0) {
            return(101);
        }else{
            // Connected Successfuly!
            
            $resault = array();
            
            $student = "SELECT id_no, name, mobile_phone FROM students";
            $result = $conn->query($student);
            if ($result->num_rows > 0) {
                while($row = $result->fetch_assoc()) {
                    $curr = array();
                    
                    $id_no = $row['id_no'];
                    $name = $row['name'];
                    $phone = $row['mobile_phone'];

                    array_push($curr, $id_no);
                    array_push($curr, $name);
                    array_push($curr, $phone);

                    array_push($resault, $curr);
                }
                
                return($resault);
            } else {
                return(0);
            }
        }
    }
    
    function deliver_student(){
        $students = $this->see_soft_student();
        $stu_num = sizeof($students);
        $counter = 0;
        
        while($counter < $stu_num){
            
            $id_no = $students[$counter][0];
            $name = $students[$counter][1];
            $phone = $students[$counter][2];
            
            $save = $this->save_student($id_no, $name, $phone);
            
            $counter = $counter+1;
        }
    }
}


?>