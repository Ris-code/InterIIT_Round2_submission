function [Phi]=funcQuat2Angle(q)

[psi, theta, phi]=quat2angle(q');

%Rearrange
Phi = [phi;theta;psi];