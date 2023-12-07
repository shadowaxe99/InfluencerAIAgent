// Influencer Service

// This service would interact with the database to manage influencer data

exports.findAllInfluencers = async () => {
  try {
    const db = await mongodb.connect(process.env.DB_CONNECTION);
    return await db.collection('influencers').find().toArray();
  } catch (error) {
    console.error('Error finding all influencers:', error);
    throw error;
  }
};

exports.createInfluencer = async (influencerData) => {
  try {
    const db = await mongodb.connect(process.env.DB_CONNECTION);
    const result = await db.collection('influencers').insertOne(influencerData);
    return result.ops[0];
  } catch (error) {
    console.error('Error creating influencer:', error);
    throw error;
  }
};

exports.updateInfluencer = async (id, influencerData) => {
  try {
    const db = await mongodb.connect(process.env.DB_CONNECTION);
    const result = await db.collection('influencers').updateOne({ _id: id }, { $set: influencerData });
    if (result.matchedCount === 0) throw new Error('No influencer found with that ID');
    return { updated: true, id: id };
  } catch (error) {
    console.error('Error updating influencer:', error);
    throw error;
  }
};

exports.deleteInfluencer = async (id) => {
  try {
    const db = await mongodb.connect(process.env.DB_CONNECTION);
    const result = await db.collection('influencers').deleteOne({ _id: id });
    if (result.deletedCount === 0) throw new Error('No influencer found with that ID to delete');
    return { deleted: true, id: id };
  } catch (error) {
    console.error('Error deleting influencer:', error);
    throw error;
  }
};
