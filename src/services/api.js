import axios from 'axios';

const API_BASE_URL = '/api';

export const getInfluencers = async () => {
  try {
    const response = await axios.get(`${API_BASE_URL}/influencers`);
    return response.data;
  } catch (error) {
    // Handle error
    console.error('Error fetching influencers:', error);
  }
};

export const createInfluencer = async (influencerData) => {
  try {
    const response = await axios.post(`${API_BASE_URL}/influencers`, influencerData);
    return response.data;
  } catch (error) {
    // Handle error
    console.error('Error creating influencer:', error);
  }
};

export const updateInfluencer = async (id, influencerData) => {
  try {
    const response = await axios.put(`${API_BASE_URL}/influencers/${id}`, influencerData);
    return response.data;
  } catch (error) {
    // Handle error
    console.error('Error updating influencer:', error);
  }
};

export const deleteInfluencer = async (id) => {
  try {
    const response = await axios.delete(`${API_BASE_URL}/influencers/${id}`);
    return response.data;
  } catch (error) {
    // Handle error
    console.error('Error deleting influencer:', error);
  }
};