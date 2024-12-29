import { AxiosInstance, CreateAxiosDefaults } from 'axios';
import axios from 'axios';
export default defineNuxtPlugin(() => {
   const {
    public: { axios: axiosConfig },
  } = useRuntimeConfig();
  const defaultAxios: CreateAxiosDefaults = {
    ...axiosConfig,
  };
  const Axios: AxiosInstance = axios.create(defaultAxios);
 return {
    provide: {
      axios: Axios,
     },
  };
});