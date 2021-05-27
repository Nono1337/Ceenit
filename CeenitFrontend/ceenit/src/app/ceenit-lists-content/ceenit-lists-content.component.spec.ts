import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CeenitListsContentComponent } from './ceenit-lists-content.component';

describe('CeenitListsContentComponent', () => {
  let component: CeenitListsContentComponent;
  let fixture: ComponentFixture<CeenitListsContentComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ CeenitListsContentComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(CeenitListsContentComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
