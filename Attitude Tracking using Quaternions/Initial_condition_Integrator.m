clear
clc
close all

load('p.mat')
load('q.mat')
load('r.mat')
load('t.mat')

%Define initial conditions for Euler Angles
phi0=0;
theta0=0.0059;
psi0=0;

%Define initial quaternion for Quaternion kinematical equation
q0=angle2quat(psi0, theta0, phi0);