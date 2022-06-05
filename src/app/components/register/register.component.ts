

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
  user: User = new User()
  submitted = false;
  Roles: any = ['Admin', 'Author', 'Reader', 'Supervisor'];

constructor(private userService: UserService, private router: Router,private route: ActivatedRoute) {}

  ngOnInit(): void {
    this.user = new User()
  }

  save() {
    this.userService.registerUser(this.user).subscribe(data =>{
        console.log("data ", data)
        this.user = new User();
        this.gotoRegister()
    },
    error => console.error());

}

  onSubmit(){
    this.submitted = true;
      this.save()

  }

  gotoRegister() {
    this.router.navigate(['/register']);
}

}
