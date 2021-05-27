import { Component, OnInit } from '@angular/core';
import { MatSort} from '@angular/material/sort';
import { MatTableDataSource} from '@angular/material/table';
import { HttpServiceService } from 'src/app/service/http-service.service';
import { ActivatedRoute } from '@angular/router';
<<<<<<< HEAD
import { Movie } from '../Model/movie.model';
import { MovieList } from '../Model/MovieList.model'
=======
import { MovieList } from '../Model/movie.model';
>>>>>>> 0d251c847d05df4339a5a38b21a3bb9318dfc01d

@Component({
  selector: 'app-ceenit-lists',
  templateUrl: './ceenit-lists.component.html',
  styleUrls: ['./ceenit-lists.component.css']
})
export class CeenitListsComponent implements OnInit {

  Lists : MovieList[];
  constructor(private httpServe: HttpServiceService, private route: ActivatedRoute) {}

  ngOnInit(): void {
    this.Lists = new Array<Movie>();
    this.httpServe
      .getMovieLists()
      .subscribe((resp) => {
        console.log(resp);
        if (resp != undefined) {
          // @ts-ignore: TS2339
          resp.forEach((movieList) => {
            this.Lists.push(movieList);
          });
        }
      });
  }

}
