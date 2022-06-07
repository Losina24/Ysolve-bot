import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AltSectionComponent } from './alt-section.component';

describe('AltSectionComponent', () => {
  let component: AltSectionComponent;
  let fixture: ComponentFixture<AltSectionComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AltSectionComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(AltSectionComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('Componente generado correctamente', () => {
    expect(component).toBeTruthy();
  });
});
