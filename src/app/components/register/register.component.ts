

import { Component, OnInit } from '@angular/core';

import { User } from "../user";
import { Router } from '@angular/router';
import { UserService } from "../user.service";
import { ActivatedRoute } from '@angular/router';


@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css'],
})
export class RegisterComponent implements OnInit {
  _id!: string;
  user!: User;
  Roles: any = ['Admin', 'Author', 'Reader', 'Supervisor'];

 

constructor(private userService: UserService, private router: Router,private route: ActivatedRoute) {}

  ngOnInit(): void {
    this.user = new User()
    this._id = this.route.snapshot.params["_id"]
    this.userService.getUser(this._id).subscribe((data: any) =>{

      this.user = data;
    },(error: any) => console.log(error));
    

    
  }

  updateUser() {

    this.userService.updateUser(this._id, this.user).subscribe( (data: any) => {
      console.log("Update User Component File", data)
      this.user = new User();
      
    }, (error: any) => console.log(error));

    
      
  }
  onSubmit(){
    this.updateUser();
  }

}
