import React from "react";
import { RouterProvider, createBrowserRouter, RouteObject } from "react-router-dom";
import { useAuth } from "../provider/AuthProvider";
import { ProtectedRoute } from "./ProtectedRoute";
import Home from "../pages/Home";
import Login from "../pages/Login";
import Event from "../pages/Event";
// import Login from "../pages/Login";
// import Logout from "../pages/Logout";


const Routes: React.FC = () => {
  const { token } = useAuth();

  // Define public routes accessible to all users
  const routesForPublic: RouteObject[] = [
    // {
    //   path: "/service",
    //   element: <div>Service Page</div>,
    // },
    // {
    //   path: "/about-us",
    //   element: <div>About Us</div>,
    // },
  ];

  // Define routes accessible only to authenticated users
  const routesForAuthenticatedOnly: RouteObject[] = [
    {
      path: "/",
      element: <ProtectedRoute />, // Wrap the component in ProtectedRoute
      children: [
        {
          path: "",
          element: <Home />,
        },
        // {
        //   path: "/profile",
        //   element: <div>User Profile</div>,
        // },
        {
          path: "/logout",
          element: <div>logout</div>,
        //   element: <Logout />,
        },
        {
          path: "/event",
          element: <Event />,
        }
      ],
    },
  ];

  // Define routes accessible only to non-authenticated users
  const routesForNotAuthenticatedOnly: RouteObject[] = [
    {
      path: "/",
      element: <Home />,
    },
    {
      path: "/login",
      element: <Login />,
    },
  ];

  // Combine and conditionally include routes based on authentication status
  const router = createBrowserRouter([
    ...routesForPublic,
    ...(!token ? routesForNotAuthenticatedOnly : []),
    ...routesForAuthenticatedOnly,
  ]);

  // Provide the router configuration using RouterProvider
  return <RouterProvider router={router} />;
};

export default Routes;
